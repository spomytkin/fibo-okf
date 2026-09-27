---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trust beneficiary
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party for whose interest (benefit) an annuity, assignment (such as a letter of credit), contract, insurance policy,
      judgment, promise, trust, will, etc., is made
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N521c0f8da84e4cf0890153d85b0c2e14
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Beneficiary.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Beneficiary
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TrustBeneficiary
sources:
- id: fibo-source-2a4049b46d
  resource: references/fibo/BE/Trusts/Trusts.rdf
  sha256: 2a4049b46d7d8daeb24877203142458caefea7a26ad56d16d6dd69523f6a04f1
  title: FIBO source BE/Trusts/Trusts.rdf
title: trust beneficiary
type: Ontology Class
---

# trust beneficiary

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TrustBeneficiary>

## Definition

party for whose interest (benefit) an annuity, assignment (such as a letter of credit), contract, insurance policy, judgment, promise, trust, will, etc., is made

## Relationships

- **Subclass of**: [Beneficiary](/concepts/fibo/FND/Agreements/Agreements/Beneficiary.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N521c0f8da84e4cf0890153d85b0c2e14`

## Annotations

- **label**: trust beneficiary
- **definition**: party for whose interest (benefit) an annuity, assignment (such as a letter of credit), contract, insurance policy, judgment, promise, trust, will, etc., is made

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
