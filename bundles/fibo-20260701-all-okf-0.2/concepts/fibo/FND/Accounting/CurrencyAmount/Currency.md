---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: currency
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: medium of exchange value, defined by reference to the geographical location of the monetary authorities responsible
      for it
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: Codes for the representation of currencies and funds, ISO 4217, Eighth edition, 2015-08-01, section 3.2
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: currency unit
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: monetary unit
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMinorUnit
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode
  - filler: https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isUsedBy
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/hasTextualName
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/MeasurementUnit
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: currency
type: Ontology Class
---

# currency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency>

## Definition

medium of exchange value, defined by reference to the geographical location of the monetary authorities responsible for it

## Relationships

- **Subclass of**: [MeasurementUnit](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/MeasurementUnit>)

## Constraints

- **[hasMinorUnit](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMinorUnit.md)**: max qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasNumericCode](/concepts/fibo/FND/Accounting/CurrencyAmount/hasNumericCode.md)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[isUsedBy](<https://www.omg.org/spec/Commons/ContextualDesignators/isUsedBy>)**: some values from of type [GeopoliticalEntity](<https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity>)
- **[hasTextualName](<https://www.omg.org/spec/Commons/Designators/hasTextualName>)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: currency
- **definition**: medium of exchange value, defined by reference to the geographical location of the monetary authorities responsible for it
- **definitionOrigin**: Codes for the representation of currencies and funds, ISO 4217, Eighth edition, 2015-08-01, section 3.2
- **synonym**: currency unit
- **synonym**: monetary unit

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
