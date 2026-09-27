---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: student loan asset-backed security
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: asset-backed security based on student loan receivables
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the credit risk of the pool has been decoupled from the institution via an SPV, then student loan asset-backed
      securities are also structured finance instruments.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The main purpose behind Student Loan ABS is to diversify the risk for lenders across many investors. By pooling
      and then packaging the loans into securities and selling them to investors, agencies can spread around the default risk,
      which allows them to give out more loans and larger loans. This way, more students have access to loans, investors have
      a diversifying investment instrument, and lenders can generate consistent cash flow from their securitization and debt
      collection services.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/StudentLoanPool
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/StudentLoanAssetBackedSecurity
sources:
- id: fibo-source-bc31503fb4
  resource: references/fibo/SEC/Debt/AssetBackedSecurities.rdf
  sha256: bc31503fb47984eace3c48c15e458215440e108098254f13885985b958f90b44
  title: FIBO source SEC/Debt/AssetBackedSecurities.rdf
title: student loan asset-backed security
type: Ontology Class
---

# student loan asset-backed security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/StudentLoanAssetBackedSecurity>

## Definition

asset-backed security based on student loan receivables

## Relationships

- **Subclass of**: [AssetBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [StudentLoanPool](/concepts/fibo/SEC/Debt/AssetBackedSecurities/StudentLoanPool.md)

## Annotations

- **label** (en): student loan asset-backed security
- **definition** (en): asset-backed security based on student loan receivables
- **explanatoryNote** (en): If the credit risk of the pool has been decoupled from the institution via an SPV, then student loan asset-backed securities are also structured finance instruments.
- **explanatoryNote** (en): The main purpose behind Student Loan ABS is to diversify the risk for lenders across many investors. By pooling and then packaging the loans into securities and selling them to investors, agencies can spread around the default risk, which allows them to give out more loans and larger loans. This way, more students have access to loans, investors have a diversifying investment instrument, and lenders can generate consistent cash flow from their securitization and debt collection services.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
