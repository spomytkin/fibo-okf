---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: in assembly agency mortgage pool
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/InAssembly
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/InAssemblyAgencyMortgagePool
sources:
- id: fibo-source-2eeca2019d
  resource: references/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
  sha256: 2eeca2019d428c47ac1513eaf8db629142182da83295878f53a62e84592f6a59
  title: FIBO source BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
title: in assembly agency mortgage pool
type: Ontology Class
---

# in assembly agency mortgage pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/InAssemblyAgencyMortgagePool>

## Relationships

- **Subclass of**: [AgencyMortgagePool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool.md)

## Constraints

- **[hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)**: some values from of type [InAssembly](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/InAssembly.md)

## Annotations

- **label** (en): in assembly agency mortgage pool

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
