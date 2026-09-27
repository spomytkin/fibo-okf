---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: structured finance without principal protection
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structured finance that is a short-term note linked to an underlying asset that offers a steady stream of income
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth
      edition, 2019-10-01.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The redemption at the end of the term is determined on the basis of the performance and final fixing of the underlying
      asset: a redemption at the nominal value is guaranteed as long as the underlying asset has not touched its barrier during
      relevant barrier monitoring. If the underlying asset has touched its barrier but is again above the strike price at
      final fixing, the nominal price is also repaid. Nevertheless, if the underlying asset has touched its barrier during
      barrier monitoring and closes below the strike price at final fixing, the underlying asset is delivered or cash compensation
      paid, provided that no credit event by the reference entity has occurred. Depending on the characteristics of the product,
      either a coupon or a discount to the underlying asset can apply. A coupon is paid out regardless of the performance
      of the underlying asset, provided that no credit event by the reference entity has occurred.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: structured finance without capital protection
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/PrincipalProtectedNote.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PrincipalProtectedNote
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: structured finance without principal protection
type: Ontology Class
---

# structured finance without principal protection

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection>

## Definition

structured finance that is a short-term note linked to an underlying asset that offers a steady stream of income

## Relationships

- **Subclass of**: [StructuredFinanceInstrument](/concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md)

## Constraints

- **Disjoint with**: [PrincipalProtectedNote](/concepts/fibo/SEC/Debt/PoolBackedSecurities/PrincipalProtectedNote.md)

## Annotations

- **label** (en): structured finance without principal protection
- **definition** (en): structured finance that is a short-term note linked to an underlying asset that offers a steady stream of income
- **adaptedFrom**: ISO 10962, Securities and related financial instruments - Classification of Financial Instruments (CFI code), Fourth edition, 2019-10-01.
- **explanatoryNote** (en): The redemption at the end of the term is determined on the basis of the performance and final fixing of the underlying asset: a redemption at the nominal value is guaranteed as long as the underlying asset has not touched its barrier during relevant barrier monitoring. If the underlying asset has touched its barrier but is again above the strike price at final fixing, the nominal price is also repaid. Nevertheless, if the underlying asset has touched its barrier during barrier monitoring and closes below the strike price at final fixing, the underlying asset is delivered or cash compensation paid, provided that no credit event by the reference entity has occurred. Depending on the characteristics of the product, either a coupon or a discount to the underlying asset can apply. A coupon is paid out regardless of the performance of the underlying asset, provided that no credit event by the reference entity has occurred.
- **synonym** (en): structured finance without capital protection

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
