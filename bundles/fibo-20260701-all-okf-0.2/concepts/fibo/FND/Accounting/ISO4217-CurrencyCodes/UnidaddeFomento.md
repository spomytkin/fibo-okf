---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Unidad de Fomento
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the funds Unidad de Fomento
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMinorUnit
    value: '4'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode
    value: '990'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The CLF is a daily economically-financial unit calculated by the Central Bank of Chile according to inflation (as
      measured by the Chilean Consumer Price Index of the previous month). The value of the CLF is expressed in terms of Chilean
      Pesos per CLF. The use of CLF has been widely extended to all types of bank loans, financial investments (time deposits,
      mortgages and other public or private indexed instruments), contracts and fees in some cases.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Unidad de Fomento
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Funds
  related_to:
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/ChileanPeso.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/ChileanPeso
  - predicate: https://www.omg.org/spec/Commons/ContextualDesignators/isUsedBy
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Chile
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/UnidaddeFomento
sources:
- id: fibo-source-4a323fa733
  resource: references/fibo/FND/Accounting/ISO4217-CurrencyCodes.rdf
  sha256: 4a323fa7336e398c312a7f8afc057b57c4a92078063cdd27a8ff11fc1fe0d60c
  title: FIBO source FND/Accounting/ISO4217-CurrencyCodes.rdf
title: Unidad de Fomento
type: Ontology Individual
---

# Unidad de Fomento

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/UnidaddeFomento>

## Definition

the funds Unidad de Fomento

## Relationships

- **Related to**: [ChileanPeso](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/ChileanPeso.md)
- **Related to**: [Chile](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Chile>)

## Annotations

- **label**: Unidad de Fomento
- **definition** (en): the funds Unidad de Fomento
- **hasMinorUnit**: 4
- **hasNumericCode**: 990
- **explanatoryNote**: The CLF is a daily economically-financial unit calculated by the Central Bank of Chile according to inflation (as measured by the Chilean Consumer Price Index of the previous month). The value of the CLF is expressed in terms of Chilean Pesos per CLF. The use of CLF has been widely extended to all types of bank loans, financial investments (time deposits, mortgages and other public or private indexed instruments), contracts and fees in some cases.
- **hasTextualName**: Unidad de Fomento

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
