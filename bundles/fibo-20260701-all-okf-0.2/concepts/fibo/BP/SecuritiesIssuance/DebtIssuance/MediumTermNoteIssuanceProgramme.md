---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: medium term note issuance programme
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a program of offerings of medium term notes; a set of issues where the maturity is defined after the rest of the
      terms have been registered with some authority; these are registered up front so that then the company wants to borrow
      more money they don't have to go through the registration period but have the facility up front to issue another security.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/MediumTermNoteOffering
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/BondIssuanceProgramme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/BondIssuanceProgramme
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/MediumTermNoteIssuanceProgramme
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: medium term note issuance programme
type: Ontology Class
---

# medium term note issuance programme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/MediumTermNoteIssuanceProgramme>

## Definition

a program of offerings of medium term notes; a set of issues where the maturity is defined after the rest of the terms have been registered with some authority; these are registered up front so that then the company wants to borrow more money they don't have to go through the registration period but have the facility up front to issue another security.

## Relationships

- **Subclass of**: [BondIssuanceProgramme](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/BondIssuanceProgramme.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [MediumTermNoteOffering](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/MediumTermNoteOffering.md)

## Annotations

- **label** (en): medium term note issuance programme
- **definition** (en): a program of offerings of medium term notes; a set of issues where the maturity is defined after the rest of the terms have been registered with some authority; these are registered up front so that then the company wants to borrow more money they don't have to go through the registration period but have the facility up front to issue another security.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
