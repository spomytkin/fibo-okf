---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trust
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: fiduciary relationship and legal entity in which one party, known as a trustor, gives another party, the trustee,
      the right to hold title to and manage assets for the benefit of a third party, the beneficiary
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TrustBeneficiary
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trustee
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trustor
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TrustAgreement
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons/BusinessEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessEntity
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trust
sources:
- id: fibo-source-2a4049b46d
  resource: references/fibo/BE/Trusts/Trusts.rdf
  sha256: 2a4049b46d7d8daeb24877203142458caefea7a26ad56d16d6dd69523f6a04f1
  title: FIBO source BE/Trusts/Trusts.rdf
title: trust
type: Ontology Class
---

# trust

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trust>

## Definition

fiduciary relationship and legal entity in which one party, known as a trustor, gives another party, the trustee, the right to hold title to and manage assets for the benefit of a third party, the beneficiary

## Relationships

- **Subclass of**: [BusinessEntity](/concepts/fibo/BE/LegalEntities/LegalPersons/BusinessEntity.md)
- **Subclass of**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Constraints

- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [TrustBeneficiary](/concepts/fibo/BE/Trusts/Trusts/TrustBeneficiary.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [Trustee](/concepts/fibo/BE/Trusts/Trusts/Trustee.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [Trustor](/concepts/fibo/BE/Trusts/Trusts/Trustor.md)
- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: exact qualified cardinality 1 of type [TrustAgreement](/concepts/fibo/BE/Trusts/Trusts/TrustAgreement.md)

## Annotations

- **label**: trust
- **definition**: fiduciary relationship and legal entity in which one party, known as a trustor, gives another party, the trustee, the right to hold title to and manage assets for the benefit of a third party, the beneficiary

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
