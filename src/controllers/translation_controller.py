# src/controllers/translation_controller.py
from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

translation_controller = Blueprint("translation", __name__)


@translation_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")

        translated_text = GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(text_to_translate)

        return render_template(
            "index.html",
            languages=LanguageModel.list_dicts(),
            text_to_translate_placeholder=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated_text=translated_text,
        )

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate_placeholder="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated_text="What do you want to translate?",
    )


@translation_controller.route("/reverse", methods=["POST"])
def reverse_translation():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    reversed_translated_text = GoogleTranslator(
        source=translate_to, target=translate_from
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate_placeholder=reversed_translated_text,
        translate_from=translate_to,
        translate_to=translate_from,
        translated_text=text_to_translate,
    )
