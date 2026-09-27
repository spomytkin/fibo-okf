---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: collateral valuation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: assessment activity resulting in the valuation of real property as collateral
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/evaluates
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraiser
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/Assessments/AssessmentActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentActivity
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/CollateralValuation
sources:
- id: fibo-source-48fe43dc99
  resource: references/fibo/LOAN/LoansGeneral/LoanEvents.rdf
  sha256: 48fe43dc99b1d7ca56ee712ff80baad56b5ac6abd1e4cb8ac5342e7bdee88e6e
  title: FIBO source LOAN/LoansGeneral/LoanEvents.rdf
title: collateral valuation
type: Ontology Class
---

# collateral valuation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/CollateralValuation>

## Definition

assessment activity resulting in the valuation of real property as collateral

## Relationships

- **Subclass of**: [AssessmentActivity](/concepts/fibo/FND/Arrangements/Assessments/AssessmentActivity.md)

## Constraints

- **[evaluates](/concepts/fibo/FND/Relations/Relations/evaluates.md)**: all values from of type [Collateral](/concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [Appraiser](/concepts/fibo/FND/Arrangements/Assessments/Appraiser.md)

## Annotations

- **label** (en): collateral valuation
- **definition** (en): assessment activity resulting in the valuation of real property as collateral

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
