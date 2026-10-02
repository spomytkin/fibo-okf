---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Uruguay Peso en Unidades Indexadas (UI)
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the funds Uruguay Peso en Unidades Indexadas (UI)
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMinorUnit
    value: '0'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode
    value: '940'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The UYI (URUIURUI) is used for issuance of debt instruments by the Uruguayan government in the international global
      bond market. It is calculated based on an established methodology using underlying inflationary statistics in the Uruguayan
      market. (Introduced in 2002).
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Uruguay Peso en Unidades Indexadas (UI)
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Funds
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/PesoUruguayo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/PesoUruguayo
  - predicate: https://www.omg.org/spec/Commons/ContextualDesignators/isUsedBy
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Uruguay
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/UruguayPesoenUnidadesIndexadas_UI
sources:
- id: fibo-source-4a323fa733
  resource: references/fibo/FND/Accounting/ISO4217-CurrencyCodes.rdf
  sha256: 4a323fa7336e398c312a7f8afc057b57c4a92078063cdd27a8ff11fc1fe0d60c
  title: FIBO source FND/Accounting/ISO4217-CurrencyCodes.rdf
title: Uruguay Peso en Unidades Indexadas (UI)
type: Ontology Individual
---

# Uruguay Peso en Unidades Indexadas (UI)

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/UruguayPesoenUnidadesIndexadas_UI>

## Definition

the funds Uruguay Peso en Unidades Indexadas (UI)

## Relationships

- **Related to**: [PesoUruguayo](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/PesoUruguayo.md)
- **Related to**: [Uruguay](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Uruguay>)

## Annotations

- **label**: Uruguay Peso en Unidades Indexadas (UI)
- **definition** (en): the funds Uruguay Peso en Unidades Indexadas (UI)
- **hasMinorUnit**: 0
- **hasNumericCode**: 940
- **explanatoryNote**: The UYI (URUIURUI) is used for issuance of debt instruments by the Uruguayan government in the international global bond market. It is calculated based on an established methodology using underlying inflationary statistics in the Uruguayan market. (Introduced in 2002).
- **hasTextualName**: Uruguay Peso en Unidades Indexadas (UI)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
