---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: multi-name credit default swap
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit default swap that references more than one obligation or borrower
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Draft paper on Credit Default Swaps from the Federal Reserve Board, available at https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For instance, a multiname contract could be written to cover defaults in a reference portfolio (such as in the
      case of a basket credit default swap) or, as has been increasingly common over the past couple of decades,be based on
      an index of commonly negotiated single-name CDS. The latter are generally called CDS indexes.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: multiname credit default swap
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/MultiNameCreditDefaultSwap
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: multi-name credit default swap
type: Ontology Class
---

# multi-name credit default swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/MultiNameCreditDefaultSwap>

## Definition

credit default swap that references more than one obligation or borrower

## Relationships

- **Subclass of**: [CreditDefaultSwap](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md)

## Annotations

- **label** (en): multi-name credit default swap
- **definition** (en): credit default swap that references more than one obligation or borrower
- **adaptedFrom**: Draft paper on Credit Default Swaps from the Federal Reserve Board, available at https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf
- **adaptedFrom**: ISO 10962:2019, Securities and related financial instruments - Classification of financial instruments (CFI) code
- **explanatoryNote** (en): For instance, a multiname contract could be written to cover defaults in a reference portfolio (such as in the case of a basket credit default swap) or, as has been increasingly common over the past couple of decades,be based on an index of commonly negotiated single-name CDS. The latter are generally called CDS indexes.
- **synonym**: multiname credit default swap

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
