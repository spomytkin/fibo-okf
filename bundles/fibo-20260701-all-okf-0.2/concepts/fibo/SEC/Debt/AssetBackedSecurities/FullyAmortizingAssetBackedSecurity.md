---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fully amortizing asset-backed security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: asset-backed security based on a pool of debt instruments that returns principal to investors over the life of
      the security
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investinginbonds.com/learnmore.asp?catid=11&subcatid=57&id=15
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Fully amortizing asset-backed securities are designed to closely reflect the full repayment of the underlying loans
      through scheduled interest and principal payments.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These are typically backed by HELs, auto loans, manufactured-housing contracts and other fully amortizing assets.
      Prepayment risk is a key consideration with such ABS, although the rate of prepayment may vary considerably by the type
      of underlying asset.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/AssetBackedSecurities/ControlledAmortizationAssetBackedSecurity.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/ControlledAmortizationAssetBackedSecurity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/FullyAmortizingAssetBackedSecurity
sources:
- id: fibo-source-bc31503fb4
  resource: references/fibo/SEC/Debt/AssetBackedSecurities.rdf
  sha256: bc31503fb47984eace3c48c15e458215440e108098254f13885985b958f90b44
  title: FIBO source SEC/Debt/AssetBackedSecurities.rdf
title: fully amortizing asset-backed security
type: Ontology Class
---

# fully amortizing asset-backed security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/FullyAmortizingAssetBackedSecurity>

## Definition

asset-backed security based on a pool of debt instruments that returns principal to investors over the life of the security

## Relationships

- **Subclass of**: [AssetBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)

## Constraints

- **Disjoint with**: [ControlledAmortizationAssetBackedSecurity](/concepts/fibo/SEC/Debt/AssetBackedSecurities/ControlledAmortizationAssetBackedSecurity.md)
- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)

## Annotations

- **label**: fully amortizing asset-backed security
- **definition**: asset-backed security based on a pool of debt instruments that returns principal to investors over the life of the security
- **adaptedFrom**: http://www.investinginbonds.com/learnmore.asp?catid=11&subcatid=57&id=15
- **explanatoryNote**: Fully amortizing asset-backed securities are designed to closely reflect the full repayment of the underlying loans through scheduled interest and principal payments.
- **explanatoryNote**: These are typically backed by HELs, auto loans, manufactured-housing contracts and other fully amortizing assets. Prepayment risk is a key consideration with such ABS, although the rate of prepayment may vary considerably by the type of underlying asset.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
