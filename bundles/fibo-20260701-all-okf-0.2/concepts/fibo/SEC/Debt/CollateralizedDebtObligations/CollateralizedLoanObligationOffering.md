---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: collateralized loan obligation offering
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CLO offering
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/AgencyCMO
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/LoanPool
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/DebtOffering
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedLoanObligationOffering
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: collateralized loan obligation offering
type: Ontology Class
---

# collateralized loan obligation offering

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedLoanObligationOffering>

## Relationships

- **Subclass of**: [DebtOffering](/concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md)

## Constraints

- **Disjoint with**: [AgencyCMO](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/AgencyCMO.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [LoanPool](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/LoanPool.md)

## Annotations

- **label** (en): collateralized loan obligation offering
- **abbreviation** (en): CLO offering

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
