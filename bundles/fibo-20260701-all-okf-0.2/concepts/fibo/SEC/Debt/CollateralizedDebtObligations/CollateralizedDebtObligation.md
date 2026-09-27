---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: collateralized debt obligation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'structured finance constructed from a portfolio of fixed income assets including corporate loans and mortgage
      backed securities. A special purpose vehicle (SPV) issues notes to investors in order to raise funds that are invested
      in a portfolio of those fixed income assets, held by the SPV as collateral for the notes. Further notes: Collateralized
      Debt Obligation, for example, ABS CDO which consists of a portfolio of different ABS bonds, and the payments to the
      holders of these trust certificates are derived from the cash flows of the ABS bonds. This CDO instrument is part of
      a CDO issue, consisting of individual CDO instruments of a given seniority. Often referred to as tranches and slices
      (Investopedia). Investopedia: Similar in structure to a collateralized mortgage obligation (CMO) or collateralized bond
      obligation (CBO), CDOs are unique in that they represent different types of debt and credit risk. In the case of CDOs,
      these different types of debt are often referred to as ''tranches'' or ''slices''. Each slice has a different maturity
      and risk associated with it. The higher the risk, the more the CDO pays. Further details: Collateralized Debt obligations
      are securitized interests in pools of - generally non-mortgage - assets. Assets - called collateral - usually comprise
      loans or debt instruments. A CDO may be called a collateralized loan obligation (CLO) or collateralized bond obligation
      (CBO) if it holds only loans or bonds, respectively. Investors bear the credit risk of the collateral. Multiple tranches
      of securities are issued by the CDO, offering investors various maturity and credit risk characteristics.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CDO
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/isSubordinatedTo
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: collateralized debt obligation
type: Ontology Class
---

# collateralized debt obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation>

## Definition

structured finance constructed from a portfolio of fixed income assets including corporate loans and mortgage backed securities. A special purpose vehicle (SPV) issues notes to investors in order to raise funds that are invested in a portfolio of those fixed income assets, held by the SPV as collateral for the notes. Further notes: Collateralized Debt Obligation, for example, ABS CDO which consists of a portfolio of different ABS bonds, and the payments to the holders of these trust certificates are derived from the cash flows of the ABS bonds. This CDO instrument is part of a CDO issue, consisting of individual CDO instruments of a given seniority. Often referred to as tranches and slices (Investopedia). Investopedia: Similar in structure to a collateralized mortgage obligation (CMO) or collateralized bond obligation (CBO), CDOs are unique in that they represent different types of debt and credit risk. In the case of CDOs, these different types of debt are often referred to as 'tranches' or 'slices'. Each slice has a different maturity and risk associated with it. The higher the risk, the more the CDO pays. Further details: Collateralized Debt obligations are securitized interests in pools of - generally non-mortgage - assets. Assets - called collateral - usually comprise loans or debt instruments. A CDO may be called a collateralized loan obligation (CLO) or collateralized bond obligation (CBO) if it holds only loans or bonds, respectively. Investors bear the credit risk of the collateral. Multiple tranches of securities are issued by the CDO, offering investors various maturity and credit risk characteristics.

## Relationships

- **Subclass of**: [StructuredFinanceInstrument](/concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md)

## Constraints

- **[isSubordinatedTo](/concepts/fibo/SEC/Debt/DebtInstruments/isSubordinatedTo.md)**: max qualified cardinality 1 of type [CollateralizedDebtObligation](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md)

## Annotations

- **label** (en): collateralized debt obligation
- **definition** (en): structured finance constructed from a portfolio of fixed income assets including corporate loans and mortgage backed securities. A special purpose vehicle (SPV) issues notes to investors in order to raise funds that are invested in a portfolio of those fixed income assets, held by the SPV as collateral for the notes. Further notes: Collateralized Debt Obligation, for example, ABS CDO which consists of a portfolio of different ABS bonds, and the payments to the holders of these trust certificates are derived from the cash flows of the ABS bonds. This CDO instrument is part of a CDO issue, consisting of individual CDO instruments of a given seniority. Often referred to as tranches and slices (Investopedia). Investopedia: Similar in structure to a collateralized mortgage obligation (CMO) or collateralized bond obligation (CBO), CDOs are unique in that they represent different types of debt and credit risk. In the case of CDOs, these different types of debt are often referred to as 'tranches' or 'slices'. Each slice has a different maturity and risk associated with it. The higher the risk, the more the CDO pays. Further details: Collateralized Debt obligations are securitized interests in pools of - generally non-mortgage - assets. Assets - called collateral - usually comprise loans or debt instruments. A CDO may be called a collateralized loan obligation (CLO) or collateralized bond obligation (CBO) if it holds only loans or bonds, respectively. Investors bear the credit risk of the collateral. Multiple tranches of securities are issued by the CDO, offering investors various maturity and credit risk characteristics.
- **abbreviation** (en): CDO

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
