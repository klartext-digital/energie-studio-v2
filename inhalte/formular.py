# -*- coding: utf-8 -*-
"""Das Kontaktformular, an einer Stelle gepflegt."""

THEMEN = ["Heizung & Kühlung", "Lüftung & Klima", "Sanitär",
          "Gebäudeautomation", "Sanierung", "Anderes"]

def formular(einzug="      "):
    chips = "\n".join(
        '%s      <label class="chip"><input type="radio" name="thema" value="%s"><span>%s</span></label>'
        % (einzug, t.replace('&', '&amp;'), t.replace('&', '&amp;')) for t in THEMEN)
    return '''%(e)s<form class="kform" data-kontakt-form novalidate>
%(e)s  <fieldset class="kform__thema">
%(e)s    <legend class="kenn">Worum geht es?</legend>
%(e)s    <div class="kform__chips">
%(chips)s
%(e)s    </div>
%(e)s  </fieldset>

%(e)s  <div class="kform__reihe">
%(e)s    <label class="kform__feld">
%(e)s      <span class="kenn">Name</span>
%(e)s      <input type="text" name="name" autocomplete="name" required>
%(e)s    </label>
%(e)s    <label class="kform__feld">
%(e)s      <span class="kenn">E-Mail</span>
%(e)s      <input type="email" name="mail" autocomplete="email" required>
%(e)s    </label>
%(e)s  </div>

%(e)s  <div class="kform__reihe">
%(e)s    <label class="kform__feld">
%(e)s      <span class="kenn">Telefon <em>optional</em></span>
%(e)s      <input type="tel" name="tel" autocomplete="tel">
%(e)s    </label>
%(e)s    <label class="kform__feld">
%(e)s      <span class="kenn">Ort oder Objekt <em>optional</em></span>
%(e)s      <input type="text" name="ort" autocomplete="address-level2">
%(e)s    </label>
%(e)s  </div>

%(e)s  <label class="kform__feld">
%(e)s    <span class="kenn">Ihr Vorhaben</span>
%(e)s    <textarea name="text" rows="4" required></textarea>
%(e)s  </label>

%(e)s  <div class="kform__fuss">
%(e)s    <button class="btn btn--primary kform__ab" type="submit">Anfrage senden
%(e)s      <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2 8h11M9 3.5 13.5 8 9 12.5" stroke="currentColor" stroke-width="1.6"/></svg>
%(e)s    </button>
%(e)s    <p class="kform__hinweis" data-kontakt-hinweis role="status"></p>
%(e)s  </div>
%(e)s</form>''' % {"e": einzug, "chips": chips}
