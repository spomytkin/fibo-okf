---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: define mortgage pool
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/NotYetIssuedAgencyMortgagePool
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/isDefiningOf
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/DefineMortgagePool
sources:
- id: fibo-source-2eeca2019d
  resource: references/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
  sha256: 2eeca2019d428c47ac1513eaf8db629142182da83295878f53a62e84592f6a59
  title: FIBO source BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
title: define mortgage pool
type: Ontology Class
---

# define mortgage pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/DefineMortgagePool>

## Relationships

- **Subclass of**: [IssuanceProcessActivity](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md)

## Constraints

- **[isDefiningOf](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/isDefiningOf.md)**: some values from of type [NotYetIssuedAgencyMortgagePool](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/NotYetIssuedAgencyMortgagePool.md)

## Annotations

- **label** (en): define mortgage pool

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
