---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: collateralized bond obligation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structured debt security that has investment-grade bonds as its underlying assets backed by the receivables on
      high-yield or junk bonds
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CBO
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'A multitranche debt structure similar in some respects to a collateralized mortgage obligation (CMO) structure.
      Typically low-rated bonds rather than mortgages serve as the collateral. The organization creating and promoting the
      structure usually holds the underlying equity and may also collect a fee. Junk bonds are typically not investment grade,
      but because they pool several types of credit quality bonds together, they offer enough diversification to be "investment
      grade." For example high yield [emerging market] CBO which consists of a portfolio of different high yield [emerging
      market] bonds. Investopedia: Similar in structure to a collateralized mortgage obligation (CMO), but different in that
      CBOs represent different levels of credit risk, not different maturities. Defoinition Origin:Investopedia'
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyCMO
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedLoanObligationOffering.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedLoanObligationOffering
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/BondPool
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedBondObligation
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: collateralized bond obligation
type: Ontology Class
---

# collateralized bond obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedBondObligation>

## Definition

structured debt security that has investment-grade bonds as its underlying assets backed by the receivables on high-yield or junk bonds

## Relationships

- **Subclass of**: [CashCDOTranche](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche.md)

## Constraints

- **Disjoint with**: [AgencyCMO](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md)
- **Disjoint with**: [CollateralizedLoanObligationOffering](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedLoanObligationOffering.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [BondPool](/concepts/fibo/SEC/Debt/AssetBackedSecurities/BondPool.md)

## Annotations

- **label** (en): collateralized bond obligation
- **definition** (en): structured debt security that has investment-grade bonds as its underlying assets backed by the receivables on high-yield or junk bonds
- **abbreviation** (en): CBO
- **explanatoryNote** (en): A multitranche debt structure similar in some respects to a collateralized mortgage obligation (CMO) structure. Typically low-rated bonds rather than mortgages serve as the collateral. The organization creating and promoting the structure usually holds the underlying equity and may also collect a fee. Junk bonds are typically not investment grade, but because they pool several types of credit quality bonds together, they offer enough diversification to be "investment grade." For example high yield [emerging market] CBO which consists of a portfolio of different high yield [emerging market] bonds. Investopedia: Similar in structure to a collateralized mortgage obligation (CMO), but different in that CBOs represent different levels of credit risk, not different maturities. Defoinition Origin:Investopedia

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
