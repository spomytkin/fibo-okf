---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Unidad de Valor Real
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the funds Unidad de Valor Real
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMinorUnit
    value: '2'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode
    value: '970'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The UVR is a daily account unit set by the Central Bank of Colombia according to the variation in the Consumer
      Price Index of Colombia. The value of UVR is expressed in terms of Colombian Pesos per UVR. It is used to denominate
      and update mortgage loans and some public debt bonds.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Unidad de Valor Real
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Funds
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/ColombianPeso.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/ColombianPeso
  - predicate: https://www.omg.org/spec/Commons/ContextualDesignators/isUsedBy
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Colombia
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/UnidaddeValorReal
sources:
- id: fibo-source-4a323fa733
  resource: references/fibo/FND/Accounting/ISO4217-CurrencyCodes.rdf
  sha256: 4a323fa7336e398c312a7f8afc057b57c4a92078063cdd27a8ff11fc1fe0d60c
  title: FIBO source FND/Accounting/ISO4217-CurrencyCodes.rdf
title: Unidad de Valor Real
type: Ontology Individual
---

# Unidad de Valor Real

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/UnidaddeValorReal>

## Definition

the funds Unidad de Valor Real

## Relationships

- **Related to**: [ColombianPeso](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/ColombianPeso.md)
- **Related to**: [Colombia](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Colombia>)

## Annotations

- **label**: Unidad de Valor Real
- **definition** (en): the funds Unidad de Valor Real
- **hasMinorUnit**: 2
- **hasNumericCode**: 970
- **explanatoryNote**: The UVR is a daily account unit set by the Central Bank of Colombia according to the variation in the Consumer Price Index of Colombia. The value of UVR is expressed in terms of Colombian Pesos per UVR. It is used to denominate and update mortgage loans and some public debt bonds.
- **hasTextualName**: Unidad de Valor Real

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
