---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bolívar Soberano
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the currency Bolívar Soberano
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: The Bolívar Soberano (VES) is redenominated by removing six zeros from the denominations. A new currency code VED/926
      representing the new valuation (1,000,000 times old VES/928) is introduced on 1 October 2021 for any internal needs
      during the redenomination process, but is not replacing VES as the official currency code. The Central Bank of Venezuela
      will not adopt the new codes in the local system, VES/928 remains in use. The actual currency code VES/928 remains the
      valid code after 1 October 2021 to use in any future transactions to indicate the redenominated Bolívar Soberano.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMinorUnit
    value: '2'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode
    value: '926'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasNumericCode
    value: '928'
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Bolívar Soberano
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
  related_to:
  - predicate: https://www.omg.org/spec/Commons/ContextualDesignators/isUsedBy
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Venezuela
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/BolívarSoberano
sources:
- id: fibo-source-4a323fa733
  resource: references/fibo/FND/Accounting/ISO4217-CurrencyCodes.rdf
  sha256: 4a323fa7336e398c312a7f8afc057b57c4a92078063cdd27a8ff11fc1fe0d60c
  title: FIBO source FND/Accounting/ISO4217-CurrencyCodes.rdf
title: Bolívar Soberano
type: Ontology Individual
---

# Bolívar Soberano

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/BolívarSoberano>

## Definition

the currency Bolívar Soberano

## Relationships

- **Related to**: [Venezuela](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Venezuela>)

## Annotations

- **label**: Bolívar Soberano
- **definition** (en): the currency Bolívar Soberano
- **note** (en): The Bolívar Soberano (VES) is redenominated by removing six zeros from the denominations. A new currency code VED/926 representing the new valuation (1,000,000 times old VES/928) is introduced on 1 October 2021 for any internal needs during the redenomination process, but is not replacing VES as the official currency code. The Central Bank of Venezuela will not adopt the new codes in the local system, VES/928 remains in use. The actual currency code VES/928 remains the valid code after 1 October 2021 to use in any future transactions to indicate the redenominated Bolívar Soberano.
- **hasMinorUnit**: 2
- **hasNumericCode**: 926
- **hasNumericCode**: 928
- **hasTextualName**: Bolívar Soberano

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
