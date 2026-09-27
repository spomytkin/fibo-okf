---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: principal protected note
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structured finance that offers investors exposure to chosen underlying assets using various approaches and asymmetric
      pay-off profiles
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth
      edition, 2019-10-01.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'There are one or more reference entities underlying the product. Redemption is made at least in the amount of
      the conditional capital protection at maturity, provided that no credit event by the reference entity has occurred.
      Conditional capital protection only applies to the nominal amount and not to the purchase price. The general functioning
      of a capital guaranteed structured instrument is as follows: the notional amount is split into a zero bond, that will
      deliver the capital guarantee at maturity, and the difference between the zero bond''s value (= present value of the
      guarantee level at maturity) and the notional amount is used for structuring the performance component with options
      which deliver the agreed pay-off profile of the structured instrument.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: capital protected note
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/CapitalProtectedProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/CapitalProtectedProduct
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PrincipalProtectedNote
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: principal protected note
type: Ontology Class
---

# principal protected note

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PrincipalProtectedNote>

## Definition

structured finance that offers investors exposure to chosen underlying assets using various approaches and asymmetric pay-off profiles

## Relationships

- **Subclass of**: [CapitalProtectedProduct](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/CapitalProtectedProduct.md)
- **Subclass of**: [StructuredFinanceInstrument](/concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md)

## Annotations

- **label** (en): principal protected note
- **definition** (en): structured finance that offers investors exposure to chosen underlying assets using various approaches and asymmetric pay-off profiles
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth edition, 2019-10-01.
- **explanatoryNote** (en): There are one or more reference entities underlying the product. Redemption is made at least in the amount of the conditional capital protection at maturity, provided that no credit event by the reference entity has occurred. Conditional capital protection only applies to the nominal amount and not to the purchase price. The general functioning of a capital guaranteed structured instrument is as follows: the notional amount is split into a zero bond, that will deliver the capital guarantee at maturity, and the difference between the zero bond's value (= present value of the guarantee level at maturity) and the notional amount is used for structuring the performance component with options which deliver the agreed pay-off profile of the structured instrument.
- **synonym** (en): capital protected note

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
