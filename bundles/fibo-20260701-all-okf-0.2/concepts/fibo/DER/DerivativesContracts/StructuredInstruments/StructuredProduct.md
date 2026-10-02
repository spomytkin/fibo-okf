---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: structured product
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security whose cash flow characteristics depend upon one or more indices or that have embedded forwards or options
      or securities where an investor's investment return and the issuer's payment obligations are contingent on, or highly
      sensitive to, changes in the value of underlying assets, indices, interest rates or cash flows
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A structured product is a pre-packaged structured finance investment strategy based on a single security, a basket
      of securities, options, indices, commodities, debt issuance or foreign currencies, and to a lesser extent, derivatives.
      Structured products are not homogeneous - there are numerous varieties of derivatives and underlying assets - but they
      can be classified under the aside categories. Typically, a desk will employ a specialized 'structurer' to design and
      manage its structured-product offering.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: market-linked investment
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: structured instrument
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/StructuredProduct
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: structured product
type: Ontology Class
---

# structured product

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/StructuredProduct>

## Definition

security whose cash flow characteristics depend upon one or more indices or that have embedded forwards or options or securities where an investor's investment return and the issuer's payment obligations are contingent on, or highly sensitive to, changes in the value of underlying assets, indices, interest rates or cash flows

## Relationships

- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Annotations

- **label** (en): structured product
- **definition** (en): security whose cash flow characteristics depend upon one or more indices or that have embedded forwards or options or securities where an investor's investment return and the issuer's payment obligations are contingent on, or highly sensitive to, changes in the value of underlying assets, indices, interest rates or cash flows
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15
- **explanatoryNote** (en): A structured product is a pre-packaged structured finance investment strategy based on a single security, a basket of securities, options, indices, commodities, debt issuance or foreign currencies, and to a lesser extent, derivatives. Structured products are not homogeneous - there are numerous varieties of derivatives and underlying assets - but they can be classified under the aside categories. Typically, a desk will employ a specialized 'structurer' to design and manage its structured-product offering.
- **synonym** (en): market-linked investment
- **synonym** (en): structured instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
