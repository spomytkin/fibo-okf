---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trustor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that establishes a trust and places property under the protection and management of one or more trustees
      for the benefit of at least one beneficiary
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: It is not always necessary to identify the trustor who may be also be a trustee and/or one of the beneficiaries.
      In legal parlance, a trustor is called a settlor in the UK and a grantor in the US, whereas in common usage he or she
      may also be called a creator, donor, initiator, owner, or trust maker.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: grantor
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: settlor
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N94869cf4a4de49258adb932077b6b61d
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trustor
sources:
- id: fibo-source-2a4049b46d
  resource: references/fibo/BE/Trusts/Trusts.rdf
  sha256: 2a4049b46d7d8daeb24877203142458caefea7a26ad56d16d6dd69523f6a04f1
  title: FIBO source BE/Trusts/Trusts.rdf
title: trustor
type: Ontology Class
---

# trustor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trustor>

## Definition

party that establishes a trust and places property under the protection and management of one or more trustees for the benefit of at least one beneficiary

## Relationships

- **Subclass of**: [OrganizationMember](<https://www.omg.org/spec/Commons/Organizations/OrganizationMember>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: all values from of type [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N94869cf4a4de49258adb932077b6b61d`

## Annotations

- **label**: trustor
- **definition**: party that establishes a trust and places property under the protection and management of one or more trustees for the benefit of at least one beneficiary
- **explanatoryNote**: It is not always necessary to identify the trustor who may be also be a trustee and/or one of the beneficiaries. In legal parlance, a trustor is called a settlor in the UK and a grantor in the US, whereas in common usage he or she may also be called a creator, donor, initiator, owner, or trust maker.
- **synonym**: grantor
- **synonym**: settlor

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
