"""Tests for Spanish sentence Pydantic models."""

import pytest

from spanish_sentence import (
    VerbEnding,
    SpanishVerb,
    DirectObject,
    IndirectObject,
    SpanishSentence,
)


class TestSpanishVerb:
    """Tests for SpanishVerb model."""

    def test_valid_ar_verb(self):
        verb = SpanishVerb(infinitive="hablar")
        assert verb.infinitive == "hablar"
        assert verb.ending == VerbEnding.AR

    def test_valid_er_verb(self):
        verb = SpanishVerb(infinitive="comer")
        assert verb.infinitive == "comer"
        assert verb.ending == VerbEnding.ER

    def test_valid_ir_verb(self):
        verb = SpanishVerb(infinitive="vivir")
        assert verb.infinitive == "vivir"
        assert verb.ending == VerbEnding.IR

    def test_verb_strips_whitespace(self):
        verb = SpanishVerb(infinitive="  correr  ")
        assert verb.infinitive == "correr"

    def test_verb_lowercased(self):
        verb = SpanishVerb(infinitive="BAILAR")
        assert verb.infinitive == "bailar"

    def test_invalid_verb_ending(self):
        with pytest.raises(ValueError, match="must end in -ar, -er, or -ir"):
            SpanishVerb(infinitive="tengo")


class TestDirectObject:
    """Tests for DirectObject model."""

    def test_valid_direct_object(self):
        obj = DirectObject(value="una manzana")
        assert obj.value == "una manzana"

    def test_empty_direct_object_fails(self):
        with pytest.raises(ValueError, match="cannot be empty"):
            DirectObject(value="   ")


class TestIndirectObject:
    """Tests for IndirectObject model."""

    def test_valid_indirect_object(self):
        obj = IndirectObject(value="a mi madre")
        assert obj.value == "a mi madre"

    def test_empty_indirect_object_fails(self):
        with pytest.raises(ValueError, match="cannot be empty"):
            IndirectObject(value="")


class TestSpanishSentence:
    """Tests for SpanishSentence model."""

    def test_sentence_with_subject_and_verb(self):
        sentence = SpanishSentence(
            subject="El perro",
            verb=SpanishVerb(infinitive="correr")
        )
        assert sentence.to_sentence() == "El perro correr"

    def test_sentence_with_direct_object(self):
        sentence = SpanishSentence(
            subject="Maria",
            verb=SpanishVerb(infinitive="comer"),
            direct_object=DirectObject(value="una ensalada")
        )
        assert sentence.to_sentence() == "Maria comer una ensalada"

    def test_sentence_with_both_objects(self):
        sentence = SpanishSentence(
            subject="El profesor",
            verb=SpanishVerb(infinitive="escribir"),
            direct_object=DirectObject(value="una carta"),
            indirect_object=IndirectObject(value="a los estudiantes")
        )
        assert sentence.to_sentence() == "El profesor escribir una carta a los estudiantes"

    def test_empty_subject_fails(self):
        with pytest.raises(ValueError, match="cannot be empty"):
            SpanishSentence(
                subject="",
                verb=SpanishVerb(infinitive="hablar")
            )

    def test_verb_ending_accessible(self):
        sentence = SpanishSentence(
            subject="Yo",
            verb=SpanishVerb(infinitive="estudiar")
        )
        assert sentence.verb.ending == VerbEnding.AR
