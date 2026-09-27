---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: classification of financial instruments code scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classification scheme for set of codes for financial instruments that can be used globally for straight-through
      processing by all involved participants in an electronic data processing environment
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CFI code scheme
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso.org/standard/73564.html
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The ISO 10962 Securities and related financial instruments - Classification of financial instruments (CFI) code
      was developed as a solution to a number of challenges. One is to establish a series of codes which clearly classify
      financial instruments having similar features. The other is to develop a glossary of terms and provide common definitions
      which allow market participants to easily understand terminology being used.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationCode
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/ClassificationOfFinancialInstrumentsCodeScheme
sources:
- id: fibo-source-6fed3fa3dd
  resource: references/fibo/SEC/Securities/SecuritiesClassification.rdf
  sha256: 6fed3fa3ddd850e875bf020fa5eb79e1d90023fb74888e9c1856e32882bc8f76
  title: FIBO source SEC/Securities/SecuritiesClassification.rdf
title: classification of financial instruments code scheme
type: Ontology Class
---

# classification of financial instruments code scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/ClassificationOfFinancialInstrumentsCodeScheme>

## Definition

classification scheme for set of codes for financial instruments that can be used globally for straight-through processing by all involved participants in an electronic data processing environment

## Relationships

- **Subclass of**: [FinancialInstrumentClassificationScheme](/concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme.md)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [FinancialInstrumentClassificationCode](/concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationCode.md)

## Annotations

- **label**: classification of financial instruments code scheme
- **definition**: classification scheme for set of codes for financial instruments that can be used globally for straight-through processing by all involved participants in an electronic data processing environment
- **abbreviation**: CFI code scheme
- **adaptedFrom**: https://www.iso.org/standard/73564.html
- **explanatoryNote**: The ISO 10962 Securities and related financial instruments - Classification of financial instruments (CFI) code was developed as a solution to a number of challenges. One is to establish a series of codes which clearly classify financial instruments having similar features. The other is to develop a glossary of terms and provide common definitions which allow market participants to easily understand terminology being used.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
