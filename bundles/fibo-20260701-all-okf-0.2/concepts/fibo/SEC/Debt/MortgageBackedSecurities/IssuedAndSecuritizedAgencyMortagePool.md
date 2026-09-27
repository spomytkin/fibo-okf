---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issued and securitized agency mortage pool
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An agency mortgage pool which has been securitized as part of an agency Mortgage Backed Security.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/Issued
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/IssuedAndSecuritizedAgencyMortagePool
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: issued and securitized agency mortage pool
type: Ontology Class
---

# issued and securitized agency mortage pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/IssuedAndSecuritizedAgencyMortagePool>

## Definition

An agency mortgage pool which has been securitized as part of an agency Mortgage Backed Security.

## Relationships

- **Subclass of**: [AgencyMortgagePool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/AgencyMortgagePool.md)

## Constraints

- **[hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)**: some values from of type [Issued](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/Issued.md)

## Annotations

- **label** (en): issued and securitized agency mortage pool
- **definition** (en): An agency mortgage pool which has been securitized as part of an agency Mortgage Backed Security.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
