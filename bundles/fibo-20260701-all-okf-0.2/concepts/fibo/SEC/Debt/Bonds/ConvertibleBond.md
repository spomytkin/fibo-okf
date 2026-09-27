---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: convertible bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond that gives the holder the right to convert the bond into a fixed number of shares (conversion ratio) if the
      equity price rises above a specified level (strike price)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the equity price remains below the strike price throughout the term of the bond it matures and is redeemed like
      a regular bond. The conversion ratio and strike price are usually set when the convertible bond is issued.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondConversionTerms
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ConvertibleBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: convertible bond
type: Ontology Class
---

# convertible bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ConvertibleBond>

## Definition

bond that gives the holder the right to convert the bond into a fixed number of shares (conversion ratio) if the equity price rises above a specified level (strike price)

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)
- **Subclass of**: [ConvertibleSecurity](/concepts/fibo/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity.md)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: min qualified cardinality 0 of type [BondConversionTerms](/concepts/fibo/SEC/Debt/Bonds/BondConversionTerms.md)

## Annotations

- **label**: convertible bond
- **definition**: bond that gives the holder the right to convert the bond into a fixed number of shares (conversion ratio) if the equity price rises above a specified level (strike price)
- **explanatoryNote**: If the equity price remains below the strike price throughout the term of the bond it matures and is redeemed like a regular bond. The conversion ratio and strike price are usually set when the convertible bond is issued.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
