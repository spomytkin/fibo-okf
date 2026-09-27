---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: arbitrage synthetic c d o
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Arbitrage synthetic CDO deals are motivated by regulatory or practical considerations that might make a bank want
      to retain ownership of debt while achieving capital relief through CDSs. In this case, the sponsoring bank has a portfolio
      of obligations, called the reference portfolio. It retains that portfolio, but offloads its credit risk by transacting
      CDSs with the CDO.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For arbitrage synthetic deals, two advantages are - an abbreviated ramp-up period (for managed deals), and - the
      possibility that selling protection through CDSs can be less expensive than directly buying the underlying bonds. This
      is often true at the lower end of the credit spectrum.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticBalanceSheetCDO.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticBalanceSheetCDO
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/assetsManagedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/issues
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/ArbitrageCDO.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ArbitrageCDO
  - concept: /concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDO.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDO
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/ArbitrageSyntheticCDO
sources:
- id: fibo-source-141b3c40ed
  resource: references/fibo/SEC/Debt/SyntheticCDOs.rdf
  sha256: 141b3c40ed364214aed3965d9cbe9daaa58da12da50f05938bd6d436aad71e2b
  title: FIBO source SEC/Debt/SyntheticCDOs.rdf
title: arbitrage synthetic c d o
type: Ontology Class
---

# arbitrage synthetic c d o

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/ArbitrageSyntheticCDO>

## Definition

Arbitrage synthetic CDO deals are motivated by regulatory or practical considerations that might make a bank want to retain ownership of debt while achieving capital relief through CDSs. In this case, the sponsoring bank has a portfolio of obligations, called the reference portfolio. It retains that portfolio, but offloads its credit risk by transacting CDSs with the CDO.

## Relationships

- **Subclass of**: [ArbitrageCDO](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/ArbitrageCDO.md)
- **Subclass of**: [SyntheticCDO](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDO.md)

## Constraints

- **Disjoint with**: [SyntheticBalanceSheetCDO](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticBalanceSheetCDO.md)
- **[assetsManagedBy](/concepts/fibo/SEC/Debt/SyntheticCDOs/assetsManagedBy.md)**: some values from of type [CDOPortfolioManager](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager.md)
- **[issues](/concepts/fibo/SEC/Debt/SyntheticCDOs/issues.md)**: some values from of type [SyntheticCDOTranche](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche.md)

## Annotations

- **label** (en): arbitrage synthetic c d o
- **definition** (en): Arbitrage synthetic CDO deals are motivated by regulatory or practical considerations that might make a bank want to retain ownership of debt while achieving capital relief through CDSs. In this case, the sponsoring bank has a portfolio of obligations, called the reference portfolio. It retains that portfolio, but offloads its credit risk by transacting CDSs with the CDO.
- **explanatoryNote** (en): For arbitrage synthetic deals, two advantages are - an abbreviated ramp-up period (for managed deals), and - the possibility that selling protection through CDSs can be less expensive than directly buying the underlying bonds. This is often true at the lower end of the credit spectrum.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
