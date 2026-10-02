---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: float float interest rate swap
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: interest rate swap that exchanges cashflows based on two different floating interest rates
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/terms/b/basisrateswap.asp
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is a swap in which two parties swap variable interest rates based on different money markets, and this is
      usually done to limit interest-rate risk that a company faces as a result of having differing lending and borrowing
      rates.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: basis rate swap
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: float-float interest rate swap
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 2
    filler: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exchanges
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Swaps/BasisSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/BasisSwap
  - concept: /concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwap
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FloatFloatInterestRateSwap
sources:
- id: fibo-source-5fb9294d27
  resource: references/fibo/DER/RateDerivatives/IRSwaps.rdf
  sha256: 5fb9294d27a8bae5230636202cd53bbfbe286fe95b2a2f1cd10e504966176791
  title: FIBO source DER/RateDerivatives/IRSwaps.rdf
title: float float interest rate swap
type: Ontology Class
---

# float float interest rate swap

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FloatFloatInterestRateSwap>

## Definition

interest rate swap that exchanges cashflows based on two different floating interest rates

## Relationships

- **Subclass of**: [BasisSwap](/concepts/fibo/DER/DerivativesContracts/Swaps/BasisSwap.md)
- **Subclass of**: [InterestRateSwap](/concepts/fibo/DER/RateDerivatives/IRSwaps/InterestRateSwap.md)

## Constraints

- **[exchanges](/concepts/fibo/FND/Relations/Relations/exchanges.md)**: exact qualified cardinality 2 of type [FloatingInterestRateLeg](/concepts/fibo/DER/RateDerivatives/IRSwaps/FloatingInterestRateLeg.md)

## Annotations

- **label**: float float interest rate swap
- **definition**: interest rate swap that exchanges cashflows based on two different floating interest rates
- **adaptedFrom**: http://www.investopedia.com/terms/b/basisrateswap.asp
- **explanatoryNote**: This is a swap in which two parties swap variable interest rates based on different money markets, and this is usually done to limit interest-rate risk that a company faces as a result of having differing lending and borrowing rates.
- **synonym**: basis rate swap
- **synonym**: float-float interest rate swap

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
