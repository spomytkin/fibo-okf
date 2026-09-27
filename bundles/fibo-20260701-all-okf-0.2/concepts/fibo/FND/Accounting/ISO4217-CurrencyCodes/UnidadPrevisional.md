---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Unidad Previsional
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the funds Unidad Previsional
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: The Unidad Previsional (UP) is a daily accounting unit that tracks changes to the nominal wage index. The value
      of UP is expressed in terms of Uruguayan Pesos per UP, with the initial value of one peso (UYU 1.00) on 04/30/2018.
      The institution responsible for the calculation and publication is the Instituto Nacional de Estadística (National Bureau
      of Statistics) according to Law 19,608.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMinorUnit
    value: '4'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode
    value: '927'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Unidad Previsional
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Funds
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/PesoUruguayo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/PesoUruguayo
  - predicate: https://www.omg.org/spec/Commons/ContextualDesignators/isUsedBy
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Uruguay
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/UnidadPrevisional
sources:
- id: fibo-source-4a323fa733
  resource: references/fibo/FND/Accounting/ISO4217-CurrencyCodes.rdf
  sha256: 4a323fa7336e398c312a7f8afc057b57c4a92078063cdd27a8ff11fc1fe0d60c
  title: FIBO source FND/Accounting/ISO4217-CurrencyCodes.rdf
title: Unidad Previsional
type: Ontology Individual
---

# Unidad Previsional

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/UnidadPrevisional>

## Definition

the funds Unidad Previsional

## Relationships

- **Related to**: [PesoUruguayo](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/PesoUruguayo.md)
- **Related to**: [Uruguay](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Uruguay>)

## Annotations

- **label**: Unidad Previsional
- **definition** (en): the funds Unidad Previsional
- **note** (en): The Unidad Previsional (UP) is a daily accounting unit that tracks changes to the nominal wage index. The value of UP is expressed in terms of Uruguayan Pesos per UP, with the initial value of one peso (UYU 1.00) on 04/30/2018. The institution responsible for the calculation and publication is the Instituto Nacional de Estadística (National Bureau of Statistics) according to Law 19,608.
- **hasMinorUnit**: 4
- **hasNumericCode**: 927
- **hasTextualName**: Unidad Previsional

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
