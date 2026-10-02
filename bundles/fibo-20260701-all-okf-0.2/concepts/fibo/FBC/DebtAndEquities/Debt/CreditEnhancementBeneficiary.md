---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: credit enhancement beneficiary
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that benefits from the collateral or guarantee established under the agreement, i.e., that is protected against
      counterparty credit risk because the collateral or guarantee serves as security for the obligation(s) owed to them
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N8d0509f99bef400ea0daff82ff85f7a5
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Beneficiary.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Beneficiary
  - concept: /concepts/fibo/FND/Agreements/Contracts/Counterparty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Counterparty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditEnhancementBeneficiary
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: credit enhancement beneficiary
type: Ontology Class
---

# credit enhancement beneficiary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditEnhancementBeneficiary>

## Definition

party that benefits from the collateral or guarantee established under the agreement, i.e., that is protected against counterparty credit risk because the collateral or guarantee serves as security for the obligation(s) owed to them

## Relationships

- **Subclass of**: [Beneficiary](/concepts/fibo/FND/Agreements/Agreements/Beneficiary.md)
- **Subclass of**: [Counterparty](/concepts/fibo/FND/Agreements/Contracts/Counterparty.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N8d0509f99bef400ea0daff82ff85f7a5`

## Annotations

- **label** (en): credit enhancement beneficiary
- **definition** (en): party that benefits from the collateral or guarantee established under the agreement, i.e., that is protected against counterparty credit risk because the collateral or guarantee serves as security for the obligation(s) owed to them

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
