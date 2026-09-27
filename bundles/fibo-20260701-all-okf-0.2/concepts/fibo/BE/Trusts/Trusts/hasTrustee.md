---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has trustee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links a trust to a named trustee
  domain:
  - concept: /concepts/fibo/BE/Trusts/Trusts/Trust.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trust
  inverse_of:
  - concept: /concepts/fibo/BE/Trusts/Trusts/isTrusteeOf.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/isTrusteeOf
  range:
  - concept: /concepts/fibo/BE/Trusts/Trusts/Trustee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trustee
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/hasTrustee
sources:
- id: fibo-source-2a4049b46d
  resource: references/fibo/BE/Trusts/Trusts.rdf
  sha256: 2a4049b46d7d8daeb24877203142458caefea7a26ad56d16d6dd69523f6a04f1
  title: FIBO source BE/Trusts/Trusts.rdf
title: has trustee
type: Ontology Property
---

# has trustee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/hasTrustee>

## Definition

links a trust to a named trustee

## Relationships

- **Domain**: [Trust](/concepts/fibo/BE/Trusts/Trusts/Trust.md)
- **Inverse of**: [isTrusteeOf](/concepts/fibo/BE/Trusts/Trusts/isTrusteeOf.md)
- **Range**: [Trustee](/concepts/fibo/BE/Trusts/Trusts/Trustee.md)
- **Subproperty of**: [isAffectedBy](<https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy>)

## Annotations

- **label**: has trustee
- **definition**: links a trust to a named trustee

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
