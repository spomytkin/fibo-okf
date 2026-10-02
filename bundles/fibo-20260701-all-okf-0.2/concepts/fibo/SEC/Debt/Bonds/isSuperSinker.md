---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: super sinker
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates that the bond has a long-term coupon but short potential short maturity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Super-sinker is a colloquial term for a term maturity, usually from a single family mortgage revenue issue with
      several term maturities, that will be the first to be called from a sinking fund into which all proceeds from prepayments
      of mortgages financed by the issue are deposited. The maturity's priority status under the call provisions means that
      it is likely to be redeemed in its entirety well before the stated maturity date.
  domain:
  - concept: /concepts/fibo/SEC/Debt/Bonds/SinkingFundAmortizationTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SinkingFundAmortizationTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isSuperSinker
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: super sinker
type: Ontology Property
---

# super sinker

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isSuperSinker>

## Definition

indicates that the bond has a long-term coupon but short potential short maturity

## Relationships

- **Domain**: [SinkingFundAmortizationTerms](/concepts/fibo/SEC/Debt/Bonds/SinkingFundAmortizationTerms.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: super sinker
- **definition**: indicates that the bond has a long-term coupon but short potential short maturity
- **explanatoryNote**: Super-sinker is a colloquial term for a term maturity, usually from a single family mortgage revenue issue with several term maturities, that will be the first to be called from a sinking fund into which all proceeds from prepayments of mortgages financed by the issue are deposited. The maturity's priority status under the call provisions means that it is likely to be redeemed in its entirety well before the stated maturity date.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
