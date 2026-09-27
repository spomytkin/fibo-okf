---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: time deposit open account
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: time deposit account that allows deposits (other than time certificates of deposit) for which there is in force
      a written contract with the depositor that neither the whole nor any part of such deposit may be withdrawn prior to
      (1) the date of maturity, which shall be not less than seven days after the date of the deposit, or (2) the expiration
      of a specified period of written notice of not less than seven days
  disjoint_with:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TimeCertificateOfDepositAccount.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TimeCertificateOfDepositAccount
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TimeDepositAccount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TimeDepositAccount
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TimeDepositOpenAccount
sources:
- id: fibo-source-482b0902cf
  resource: references/fibo/FBC/ProductsAndServices/ClientsAndAccounts.rdf
  sha256: 482b0902cf20a3e1d57ebf2e63481513a501ece098a0e4ff00ac78ae9ff430dc
  title: FIBO source FBC/ProductsAndServices/ClientsAndAccounts.rdf
title: time deposit open account
type: Ontology Class
---

# time deposit open account

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TimeDepositOpenAccount>

## Definition

time deposit account that allows deposits (other than time certificates of deposit) for which there is in force a written contract with the depositor that neither the whole nor any part of such deposit may be withdrawn prior to (1) the date of maturity, which shall be not less than seven days after the date of the deposit, or (2) the expiration of a specified period of written notice of not less than seven days

## Relationships

- **Subclass of**: [TimeDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TimeDepositAccount.md)

## Constraints

- **Disjoint with**: [TimeCertificateOfDepositAccount](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/TimeCertificateOfDepositAccount.md)

## Annotations

- **label**: time deposit open account
- **definition**: time deposit account that allows deposits (other than time certificates of deposit) for which there is in force a written contract with the depositor that neither the whole nor any part of such deposit may be withdrawn prior to (1) the date of maturity, which shall be not less than seven days after the date of the deposit, or (2) the expiration of a specified period of written notice of not less than seven days

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
