---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial instrument classifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for a financial instrument based on its type and features
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples include equity instrument, debt instrument, option, future, etc. per the the ISO 10962 CFI (Classification
      of Financial Instruments) standard, as cash instruments or derivative instruments per the Financial Accounting Standards
      Board (FASB) and International Accounting Standards Board (IASB) accounting standards, and so forth.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier
sources:
- id: fibo-source-6fed3fa3dd
  resource: references/fibo/SEC/Securities/SecuritiesClassification.rdf
  sha256: 6fed3fa3ddd850e875bf020fa5eb79e1d90023fb74888e9c1856e32882bc8f76
  title: FIBO source SEC/Securities/SecuritiesClassification.rdf
title: financial instrument classifier
type: Ontology Class
---

# financial instrument classifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier>

## Definition

classifier for a financial instrument based on its type and features

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: exact qualified cardinality 1 of type [FinancialInstrumentClassificationScheme](/concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme.md)

## Annotations

- **label**: financial instrument classifier
- **definition**: classifier for a financial instrument based on its type and features
- **example**: Examples include equity instrument, debt instrument, option, future, etc. per the the ISO 10962 CFI (Classification of Financial Instruments) standard, as cash instruments or derivative instruments per the Financial Accounting Standards Board (FASB) and International Accounting Standards Board (IASB) accounting standards, and so forth.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
