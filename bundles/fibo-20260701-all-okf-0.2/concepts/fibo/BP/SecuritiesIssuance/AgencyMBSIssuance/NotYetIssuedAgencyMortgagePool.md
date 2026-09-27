---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: not yet issued agency mortgage pool
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/NotYetIssued
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/NotYetIssuedAgencyMortgagePool
sources:
- id: fibo-source-2eeca2019d
  resource: references/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
  sha256: 2eeca2019d428c47ac1513eaf8db629142182da83295878f53a62e84592f6a59
  title: FIBO source BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
title: not yet issued agency mortgage pool
type: Ontology Class
---

# not yet issued agency mortgage pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/NotYetIssuedAgencyMortgagePool>

## Relationships

- **Subclass of**: [AgencyMortgagePool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool.md)

## Constraints

- **[hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)**: some values from of type [NotYetIssued](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/NotYetIssued.md)

## Annotations

- **label** (en): not yet issued agency mortgage pool

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
