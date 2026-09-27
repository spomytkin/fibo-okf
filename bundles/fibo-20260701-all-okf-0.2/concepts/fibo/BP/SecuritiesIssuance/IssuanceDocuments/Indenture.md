---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: indenture
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A written contract, also known as a "Deed of Trust", under which bonds and debentures are issued, setting forth
      maturity date, interest rate, redemption rights, call privileges and other terms. Under the rules of the Trust Indenture
      Act of 1939, the contract is executed by the issuer and a trustee who acts on behalf of the bondholders.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/SecuritiesIssuanceAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/SecuritiesIssuanceAgreement
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/Indenture
sources:
- id: fibo-source-4c4b98a252
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceDocuments.rdf
  sha256: 4c4b98a25292417c0cfa751a871d67e42ea9e85f29ea26acb47bf9860bbda08e
  title: FIBO source BP/SecuritiesIssuance/IssuanceDocuments.rdf
title: indenture
type: Ontology Class
---

# indenture

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/Indenture>

## Definition

A written contract, also known as a "Deed of Trust", under which bonds and debentures are issued, setting forth maturity date, interest rate, redemption rights, call privileges and other terms. Under the rules of the Trust Indenture Act of 1939, the contract is executed by the issuer and a trustee who acts on behalf of the bondholders.

## Relationships

- **Subclass of**: [SecuritiesIssuanceAgreement](/concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/SecuritiesIssuanceAgreement.md)
- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Annotations

- **label** (en): indenture
- **definition** (en): A written contract, also known as a "Deed of Trust", under which bonds and debentures are issued, setting forth maturity date, interest rate, redemption rights, call privileges and other terms. Under the rules of the Trust Indenture Act of 1939, the contract is executed by the issuer and a trustee who acts on behalf of the bondholders.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
