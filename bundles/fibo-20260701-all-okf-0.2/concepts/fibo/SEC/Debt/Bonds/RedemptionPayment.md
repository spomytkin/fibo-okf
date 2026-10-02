---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: redemption payment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: repayment event involving payment of a bond's principal amount at maturity or when it is called
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentEvent
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/RedemptionEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/RedemptionEvent
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RedemptionPayment
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: redemption payment
type: Ontology Class
---

# redemption payment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RedemptionPayment>

## Definition

repayment event involving payment of a bond's principal amount at maturity or when it is called

## Relationships

- **Subclass of**: [PaymentEvent](/concepts/fibo/FND/ProductsAndServices/PaymentsAndSchedules/PaymentEvent.md)
- **Subclass of**: [RedemptionEvent](/concepts/fibo/SEC/Debt/DebtInstruments/RedemptionEvent.md)

## Annotations

- **label**: redemption payment
- **definition**: repayment event involving payment of a bond's principal amount at maturity or when it is called

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
