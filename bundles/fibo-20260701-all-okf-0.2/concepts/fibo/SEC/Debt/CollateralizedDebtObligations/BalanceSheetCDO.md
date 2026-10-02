---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: balance sheet c d o
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Balance Sheet CDO/CLO/CBO - the reference assets for the SDO portfolio are taken from a company/firm's balance
      sheet.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: With a balance sheet deal, the sponsoring organization is a bank or other institution that holds - or anticipates
      acquiring - loans or debt that it wants to remove from its balance sheet. Similar to a traditional ABS, the CDO is a
      vehicle for it to do so. Balance Sheet CDO = Funded CDO. This is about whether or not ther is actual borrowing or lending
      underpinning the CDO. Does this have meaning in the context of synthetic CDO? It has meaning in the context of a sythetic
      CDO because you can constructt hat from a unifirm funding and use the CDSs to break up and creat the manyt risks. Derive
      the funds from a uniform source using CDSs. So that would be on Balance Sheet CDO. April 28 notes does Balance sheet
      CDPO have any meaning fo rCash =CDO? No. cash CDOs would have to have a balance sheet impact, so this distinction between
      Balance sheet and Arbittrrage only has meaning for Synthetics.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/BalanceSheetCDOObjective
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/hasCDOOriginationObjective
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/BalanceSheetCDO
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: balance sheet c d o
type: Ontology Class
---

# balance sheet c d o

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/BalanceSheetCDO>

## Definition

Balance Sheet CDO/CLO/CBO - the reference assets for the SDO portfolio are taken from a company/firm's balance sheet.

## Relationships

- **Subclass of**: [CDODeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)

## Constraints

- **[hasCDOOriginationObjective](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/hasCDOOriginationObjective.md)**: some values from of type [BalanceSheetCDOObjective](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/BalanceSheetCDOObjective.md)

## Annotations

- **label** (en): balance sheet c d o
- **definition** (en): Balance Sheet CDO/CLO/CBO - the reference assets for the SDO portfolio are taken from a company/firm's balance sheet.
- **editorialNote** (en): With a balance sheet deal, the sponsoring organization is a bank or other institution that holds - or anticipates acquiring - loans or debt that it wants to remove from its balance sheet. Similar to a traditional ABS, the CDO is a vehicle for it to do so. Balance Sheet CDO = Funded CDO. This is about whether or not ther is actual borrowing or lending underpinning the CDO. Does this have meaning in the context of synthetic CDO? It has meaning in the context of a sythetic CDO because you can constructt hat from a unifirm funding and use the CDSs to break up and creat the manyt risks. Derive the funds from a uniform source using CDSs. So that would be on Balance Sheet CDO. April 28 notes does Balance sheet CDPO have any meaning fo rCash =CDO? No. cash CDOs would have to have a balance sheet impact, so this distinction between Balance sheet and Arbittrrage only has meaning for Synthetics.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
