---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issued and securitized non agency mortgage pool
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A non agency mortgage pool which has been securitized as part of a tranched Mortgage Backed Security.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/Issued
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/NonAgencyMortgagePool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/NonAgencyMortgagePool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/IssuedAndSecuritizedNonAgencyMortgagePool
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: issued and securitized non agency mortgage pool
type: Ontology Class
---

# issued and securitized non agency mortgage pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/IssuedAndSecuritizedNonAgencyMortgagePool>

## Definition

A non agency mortgage pool which has been securitized as part of a tranched Mortgage Backed Security.

## Relationships

- **Subclass of**: [NonAgencyMortgagePool](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/NonAgencyMortgagePool.md)

## Constraints

- **[hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)**: some values from of type [Issued](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/Issued.md)

## Annotations

- **label** (en): issued and securitized non agency mortgage pool
- **definition** (en): A non agency mortgage pool which has been securitized as part of a tranched Mortgage Backed Security.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
