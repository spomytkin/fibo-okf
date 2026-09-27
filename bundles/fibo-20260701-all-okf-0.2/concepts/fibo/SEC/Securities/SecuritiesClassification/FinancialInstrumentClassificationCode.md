---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial instrument classification code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier and code for a financial instrument defined in the ISO 10962 Classification of Financial Instruments
      (CFI) Code Scheme
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CFI code
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso.org/standard/73564.html
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/ClassificationOfFinancialInstrumentsCodeScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationCode
sources:
- id: fibo-source-6fed3fa3dd
  resource: references/fibo/SEC/Securities/SecuritiesClassification.rdf
  sha256: 6fed3fa3ddd850e875bf020fa5eb79e1d90023fb74888e9c1856e32882bc8f76
  title: FIBO source SEC/Securities/SecuritiesClassification.rdf
title: financial instrument classification code
type: Ontology Class
---

# financial instrument classification code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationCode>

## Definition

classifier and code for a financial instrument defined in the ISO 10962 Classification of Financial Instruments (CFI) Code Scheme

## Relationships

- **Subclass of**: [FinancialInstrumentClassifier](/concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)

## Constraints

- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: exact qualified cardinality 1 of type [ClassificationOfFinancialInstrumentsCodeScheme](/concepts/fibo/SEC/Securities/SecuritiesClassification/ClassificationOfFinancialInstrumentsCodeScheme.md)

## Annotations

- **label**: financial instrument classification code
- **definition**: classifier and code for a financial instrument defined in the ISO 10962 Classification of Financial Instruments (CFI) Code Scheme
- **abbreviation**: CFI code
- **adaptedFrom**: https://www.iso.org/standard/73564.html

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
