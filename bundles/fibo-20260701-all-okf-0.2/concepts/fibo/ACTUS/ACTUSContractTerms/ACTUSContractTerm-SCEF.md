---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - SCEF
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: scalingEffect
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Indicates which payments are scaled. I = Interest payments, N = Nominal payments and M = Maximum deferred interest
      amount. They can be scaled in any combination.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: SCEF
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Scaling Effect
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-SCEF
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - SCEF
type: Ontology Individual
---

# ACTUS contract term - SCEF

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-SCEF>

## Relationships

- **Related to**: [ACTUSContractTermGroup-NotionalPrincipal](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-NotionalPrincipal.md)

## Annotations

- **label**: ACTUS contract term - SCEF
- **hasParameterName**: scalingEffect
- **hasDescription**: Indicates which payments are scaled. I = Interest payments, N = Nominal payments and M = Maximum deferred interest amount. They can be scaled in any combination.
- **hasTag**: SCEF
- **hasTextualName**: Scaling Effect

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
