---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: forward rate agreement
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: agreement to exchange an interest rate commitment on a notional amount at a future date
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FRA
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The FRA determines the rates to be used along with the termination date and notional value. FRAs are cash-settled
      with the payment based on the net difference between the interest rate of the contract and the floating rate in the
      market called the reference rate. The notional amount is not exchanged, but rather a cash amount based on the rate differentials
      and the notional value of the contract.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ForwardRateAgreement
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
title: forward rate agreement
type: Ontology Class
---

# forward rate agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ForwardRateAgreement>

## Definition

agreement to exchange an interest rate commitment on a notional amount at a future date

## Relationships

- **Subclass of**: [InterestRateDerivative](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md)

## Annotations

- **label** (en): forward rate agreement
- **definition** (en): agreement to exchange an interest rate commitment on a notional amount at a future date
- **abbreviation** (en): FRA
- **explanatoryNote** (en): The FRA determines the rates to be used along with the termination date and notional value. FRAs are cash-settled with the payment based on the net difference between the interest rate of the contract and the floating rate in the market called the reference rate. The notional amount is not exchanged, but rather a cash amount based on the rate differentials and the notional value of the contract.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
