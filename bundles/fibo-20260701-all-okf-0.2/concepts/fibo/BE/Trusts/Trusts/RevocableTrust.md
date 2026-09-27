---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: revocable trust
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: trust in which legal ownership of the trust property is transferred to the trustee, but the trustor retains full
      power to revoke, modify or amend the trust
  disjoint_with:
  - concept: /concepts/fibo/BE/Trusts/Trusts/IrrevocableTrust.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/IrrevocableTrust
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/Trusts/Trusts/Trust.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trust
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/RevocableTrust
sources:
- id: fibo-source-2a4049b46d
  resource: references/fibo/BE/Trusts/Trusts.rdf
  sha256: 2a4049b46d7d8daeb24877203142458caefea7a26ad56d16d6dd69523f6a04f1
  title: FIBO source BE/Trusts/Trusts.rdf
title: revocable trust
type: Ontology Class
---

# revocable trust

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/RevocableTrust>

## Definition

trust in which legal ownership of the trust property is transferred to the trustee, but the trustor retains full power to revoke, modify or amend the trust

## Relationships

- **Subclass of**: [Trust](/concepts/fibo/BE/Trusts/Trusts/Trust.md)

## Constraints

- **Disjoint with**: [IrrevocableTrust](/concepts/fibo/BE/Trusts/Trusts/IrrevocableTrust.md)

## Annotations

- **label**: revocable trust
- **definition**: trust in which legal ownership of the trust property is transferred to the trustee, but the trustor retains full power to revoke, modify or amend the trust

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
