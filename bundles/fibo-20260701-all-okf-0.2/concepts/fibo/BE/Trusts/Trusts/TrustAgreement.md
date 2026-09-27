---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trust agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal agreement that establishes a trust, whereby the trustor(s) gives the trustee(s) the responsibility to hold
      and manage assets for the beneficiary(ies)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A trust agreement typically states the (1) purpose for which the trust was established and fulfillment of which
      will terminate the trust, (2) details of the assets placed in the trust, (3) powers and limitations of the trustees,
      their reporting requirements, and other associated provisions, and (4) may also specify the trustees' compensation,
      if any. A trust agreement involving real estate requires its exact description and the trustor's express, written consent
      to create the trust to be valid.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: trust deed
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: trust document
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: trust instrument
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
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TrustAgreement
sources:
- id: fibo-source-2a4049b46d
  resource: references/fibo/BE/Trusts/Trusts.rdf
  sha256: 2a4049b46d7d8daeb24877203142458caefea7a26ad56d16d6dd69523f6a04f1
  title: FIBO source BE/Trusts/Trusts.rdf
title: trust agreement
type: Ontology Class
---

# trust agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TrustAgreement>

## Definition

formal agreement that establishes a trust, whereby the trustor(s) gives the trustee(s) the responsibility to hold and manage assets for the beneficiary(ies)

## Relationships

- **Subclass of**: [OrganizationCoveringAgreement](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement.md)

## Constraints

- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [TrustBeneficiary](/concepts/fibo/BE/Trusts/Trusts/TrustBeneficiary.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [Trustee](/concepts/fibo/BE/Trusts/Trusts/Trustee.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [Trustor](/concepts/fibo/BE/Trusts/Trusts/Trustor.md)

## Annotations

- **label**: trust agreement
- **definition**: formal agreement that establishes a trust, whereby the trustor(s) gives the trustee(s) the responsibility to hold and manage assets for the beneficiary(ies)
- **explanatoryNote**: A trust agreement typically states the (1) purpose for which the trust was established and fulfillment of which will terminate the trust, (2) details of the assets placed in the trust, (3) powers and limitations of the trustees, their reporting requirements, and other associated provisions, and (4) may also specify the trustees' compensation, if any. A trust agreement involving real estate requires its exact description and the trustor's express, written consent to create the trust to be valid.
- **synonym**: trust deed
- **synonym**: trust document
- **synonym**: trust instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
