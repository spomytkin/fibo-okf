---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Mexican Unidad de Inversion (UDI)
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the funds Mexican Unidad de Inversion (UDI)
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMinorUnit
    value: '2'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode
    value: '979'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The UDI is an inflation adjusted mechanism set by the Central Bank of Mexico according to the variation in the
      Mexican Consumer Price Index. The value of the UDI is expressed in terms of Mexican Pesos per UDI. It is used to denominate
      mortgage loans, some bank deposits with maturities of 3 month or more and Government bonds (UDIBONOS).
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Mexican Unidad de Inversion (UDI)
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Funds
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/MexicanPeso.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/MexicanPeso
  - predicate: https://www.omg.org/spec/Commons/ContextualDesignators/isUsedBy
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Mexico
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/MexicanUnidaddeInversion_UDI
sources:
- id: fibo-source-4a323fa733
  resource: references/fibo/FND/Accounting/ISO4217-CurrencyCodes.rdf
  sha256: 4a323fa7336e398c312a7f8afc057b57c4a92078063cdd27a8ff11fc1fe0d60c
  title: FIBO source FND/Accounting/ISO4217-CurrencyCodes.rdf
title: Mexican Unidad de Inversion (UDI)
type: Ontology Individual
---

# Mexican Unidad de Inversion (UDI)

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/MexicanUnidaddeInversion_UDI>

## Definition

the funds Mexican Unidad de Inversion (UDI)

## Relationships

- **Related to**: [MexicanPeso](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/MexicanPeso.md)
- **Related to**: [Mexico](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Mexico>)

## Annotations

- **label**: Mexican Unidad de Inversion (UDI)
- **definition** (en): the funds Mexican Unidad de Inversion (UDI)
- **hasMinorUnit**: 2
- **hasNumericCode**: 979
- **explanatoryNote**: The UDI is an inflation adjusted mechanism set by the Central Bank of Mexico according to the variation in the Mexican Consumer Price Index. The value of the UDI is expressed in terms of Mexican Pesos per UDI. It is used to denominate mortgage loans, some bank deposits with maturities of 3 month or more and Government bonds (UDIBONOS).
- **hasTextualName**: Mexican Unidad de Inversion (UDI)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
