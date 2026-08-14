<?php
/**
 * Nimmt die Anfrage aus dem Kontaktformular entgegen und schickt sie weiter.
 *
 * Absender: NICHT die Adresse des Besuchers und auch nicht hello@energie-studio.ch.
 * Die Domain erlaubt per SPF nur Microsoft als Versender ("-all"); eine Mail
 * vom Webserver mit dieser Absenderadresse landet sonst im Spam. Deshalb
 * verschickt der Server unter seiner eigenen Adresse und traegt den Besucher
 * als Antwortadresse ein — ein Klick auf "Antworten" geht direkt an ihn.
 */

declare(strict_types=1);

const EMPFAENGER = 'hello@energie-studio.ch';
// Muss zur Domain des Servers passen, sonst greift dessen Spam-Schutz.
const ABSENDER   = 'website@energie-studio.ch';
const MINDESTZEIT = 3;   // Sekunden; schneller fuellt kein Mensch ein Formular aus

header('Content-Type: application/json; charset=utf-8');

function antwort(int $code, string $text, bool $ok = false): void {
    http_response_code($code);
    echo json_encode(['ok' => $ok, 'text' => $text], JSON_UNESCAPED_UNICODE);
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    antwort(405, 'Nur über das Formular.');
}

/** Zeilenumbrueche raus: sonst liessen sich zusaetzliche Kopfzeilen einschleusen. */
function sauber(string $w, int $max = 300): string {
    $w = str_replace(["\r", "\n", "%0a", "%0d"], ' ', $w);
    return mb_substr(trim($w), 0, $max);
}

$name = sauber($_POST['name'] ?? '', 120);
$mail = sauber($_POST['mail'] ?? '', 160);
$tel  = sauber($_POST['tel']  ?? '', 60);
$text = trim((string)($_POST['text'] ?? ''));
$topf = trim((string)($_POST['website'] ?? ''));   // Falle: bleibt beim Menschen leer
$zeit = (int)($_POST['zeit'] ?? 0);

if ($topf !== '') {
    // Automat erkannt. Freundlich bestaetigen, nichts verschicken.
    antwort(200, 'Danke, Ihre Anfrage ist unterwegs.', true);
}
if ($zeit > 0 && (time() - $zeit) < MINDESTZEIT) {
    antwort(422, 'Bitte einen Moment und dann erneut senden.');
}
if ($name === '' || $mail === '' || $text === '') {
    antwort(422, 'Bitte Name, E-Mail und Ihr Vorhaben ausfüllen.');
}
if (!filter_var($mail, FILTER_VALIDATE_EMAIL)) {
    antwort(422, 'Diese E-Mail-Adresse stimmt nicht.');
}
if (mb_strlen($text) > 5000) {
    antwort(422, 'Die Nachricht ist zu lang.');
}

$betreff = 'Anfrage von ' . $name;
$koerper = $text . "\n\n"
         . "— — —\n"
         . "Name: $name\n"
         . "E-Mail: $mail\n"
         . ($tel !== '' ? "Telefon: $tel\n" : '')
         . 'Gesendet: ' . date('d.m.Y H:i') . "\n"
         . 'Seite: ' . sauber((string)($_SERVER['HTTP_REFERER'] ?? '-'), 200) . "\n";

$kopf = [
    'From: Energie Studio Website <' . ABSENDER . '>',
    'Reply-To: ' . $name . ' <' . $mail . '>',
    'Content-Type: text/plain; charset=UTF-8',
    'X-Mailer: energie-studio-website',
];

$erfolg = mail(
    EMPFAENGER,
    '=?UTF-8?B?' . base64_encode($betreff) . '?=',
    $koerper,
    implode("\r\n", $kopf),
    '-f' . ABSENDER
);

if (!$erfolg) {
    antwort(500, 'Der Versand hat nicht geklappt. Bitte schreiben Sie an ' . EMPFAENGER . '.');
}
antwort(200, 'Danke — Ihre Anfrage ist angekommen. Wir melden uns innerhalb von zwei Arbeitstagen.', true);
