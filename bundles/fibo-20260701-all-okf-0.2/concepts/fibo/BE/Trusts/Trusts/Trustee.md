---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trustee
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that holds and manages assets for the benefit of another
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The trustee is legally obliged to make all trust-related decisions with the beneficiary's interests in mind, and
      may be liable for damages in the event of not doing so. Trustees may be entitled to a payment for their services, if
      specified in the trust agreement. In the specific case of the bond market, a trustee administers a bond issue for a
      borrower, and ensures that the issuer meets all the terms and conditions associated with the borrowing.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N02055dd9fa6142e0a8f6ef99fbfc94a6
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N27cfd2906ffd466aa1117f52eb9b4a1d
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Naf7ec4c5d3614041be98a507a2c0ae31
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trustee
sources:
- id: fibo-source-2a4049b46d
  resource: references/fibo/BE/Trusts/Trusts.rdf
  sha256: 2a4049b46d7d8daeb24877203142458caefea7a26ad56d16d6dd69523f6a04f1
  title: FIBO source BE/Trusts/Trusts.rdf
title: trustee
type: Ontology Class
---

# trustee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trustee>

## Definition

party that holds and manages assets for the benefit of another

## Relationships

- **Subclass of**: [LegallyDelegatedAuthority](<https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority>)
- **Subclass of**: [OrganizationMember](<https://www.omg.org/spec/Commons/Organizations/OrganizationMember>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N02055dd9fa6142e0a8f6ef99fbfc94a6`
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N27cfd2906ffd466aa1117f52eb9b4a1d`
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Naf7ec4c5d3614041be98a507a2c0ae31`

## Annotations

- **label**: trustee
- **definition**: party that holds and manages assets for the benefit of another
- **explanatoryNote**: The trustee is legally obliged to make all trust-related decisions with the beneficiary's interests in mind, and may be liable for damages in the event of not doing so. Trustees may be entitled to a payment for their services, if specified in the trust agreement. In the specific case of the bond market, a trustee administers a bond issue for a borrower, and ensures that the issuer meets all the terms and conditions associated with the borrowing.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
