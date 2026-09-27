---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: barrier capital protection certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: capital-protected product whose protection is defined as a percentage of the nominal price (e.g. 100 percent),
      with minimum redemption at expiry equivalent to the capital protection
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: Note that capital protection in this case refers to the nominal amount only, and not to the purchase price. The
      value of the product may fall below its capital protection value during its lifetime; participation is in the underlying
      price increase above the strike up to the barrier; possibility of rebate payment once barrier is breached; limited profit
      potential.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15, clause 6.4.7
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/CapitalProtectedProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/CapitalProtectedProduct
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BarrierCapitalProtectionCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: barrier capital protection certificate
type: Ontology Class
---

# barrier capital protection certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BarrierCapitalProtectionCertificate>

## Definition

capital-protected product whose protection is defined as a percentage of the nominal price (e.g. 100 percent), with minimum redemption at expiry equivalent to the capital protection

## Relationships

- **Subclass of**: [CapitalProtectedProduct](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/CapitalProtectedProduct.md)
- **Subclass of**: [ParticipationCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)

## Annotations

- **label** (en): barrier capital protection certificate
- **definition** (en): capital-protected product whose protection is defined as a percentage of the nominal price (e.g. 100 percent), with minimum redemption at expiry equivalent to the capital protection
- **note** (en): Note that capital protection in this case refers to the nominal amount only, and not to the purchase price. The value of the product may fall below its capital protection value during its lifetime; participation is in the underlying price increase above the strike up to the barrier; possibility of rebate payment once barrier is breached; limited profit potential.
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15, clause 6.4.7

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
