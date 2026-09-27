---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: capital-protected product
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structured product that participates in the performance of a financial asset, such as a stock, fund or index, while
      protecting the investor's capital
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: 'Capital protected structured instruments offer investors exposure to chosen underlying assets using various approaches
      and offering a large variety of asymmetric pay-off profiles. There are one or more reference entities underlying the
      product. Redemption is made at least in the amount of the conditional capital protection at maturity, provided that
      no credit event by the reference entity has occurred. Conditional capital protection only applies to the nominal amount
      and not to the purchase price. The general functioning of a capital guaranteed structured instrument is as follows:
      the notional amount is split into a zero bond, that will deliver the capital guarantee at maturity, and the difference
      between the zero bond''s value (= present value of the guarantee level at maturity) and the notional amount is used
      for structuring the performance component with options which deliver the agreed pay-off profile of the structured instrument.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CPI
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15, clause 6.4.7
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Depending on the product, they may participate to varying degrees in the underlying asset's upside and protect
      the capital either entirely or partially.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: capital protected investment
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/StructuredProduct
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/CapitalProtectedProduct
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: capital-protected product
type: Ontology Class
---

# capital-protected product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/CapitalProtectedProduct>

## Definition

structured product that participates in the performance of a financial asset, such as a stock, fund or index, while protecting the investor's capital

## Relationships

- **Subclass of**: [StructuredProduct](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md)

## Annotations

- **label** (en): capital-protected product
- **definition** (en): structured product that participates in the performance of a financial asset, such as a stock, fund or index, while protecting the investor's capital
- **note** (en): Capital protected structured instruments offer investors exposure to chosen underlying assets using various approaches and offering a large variety of asymmetric pay-off profiles. There are one or more reference entities underlying the product. Redemption is made at least in the amount of the conditional capital protection at maturity, provided that no credit event by the reference entity has occurred. Conditional capital protection only applies to the nominal amount and not to the purchase price. The general functioning of a capital guaranteed structured instrument is as follows: the notional amount is split into a zero bond, that will deliver the capital guarantee at maturity, and the difference between the zero bond's value (= present value of the guarantee level at maturity) and the notional amount is used for structuring the performance component with options which deliver the agreed pay-off profile of the structured instrument.
- **abbreviation** (en): CPI
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15, clause 6.4.7
- **explanatoryNote** (en): Depending on the product, they may participate to varying degrees in the underlying asset's upside and protect the capital either entirely or partially.
- **synonym** (en): capital protected investment

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
