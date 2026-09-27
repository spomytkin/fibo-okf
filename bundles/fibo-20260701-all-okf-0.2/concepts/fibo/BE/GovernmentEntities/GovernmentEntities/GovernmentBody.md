---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: government body
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal organization that is an agency, instrumentality, or other body of a supranational, national, federal, state,
      or local government, including certain multijurisdictional agencies and departments that carry out the business of government
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Identifying government bodies is a pre-requisite for identifying government officials. This information is needed
      to help ensure compliance with applicable laws relating to bribery or corruption, including the U.S. Foreign Corrupt
      Practices Act (FCPA), the UK Bribery Act 2010 (UKBA), the U.S. Bank Bribery Act (Bribery Act), and other anti-bribery
      and corruption laws in the jurisdictions where financial institutions conduct business.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/PublicPurpose
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/FormalOrganization
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: government body
type: Ontology Class
---

# government body

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody>

## Definition

formal organization that is an agency, instrumentality, or other body of a supranational, national, federal, state, or local government, including certain multijurisdictional agencies and departments that carry out the business of government

## Relationships

- **Subclass of**: [FormalOrganization](<https://www.omg.org/spec/Commons/Organizations/FormalOrganization>)

## Constraints

- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: min qualified cardinality 0 of type [PublicPurpose](/concepts/fibo/BE/LegalEntities/LegalPersons/PublicPurpose.md)

## Annotations

- **label**: government body
- **definition**: formal organization that is an agency, instrumentality, or other body of a supranational, national, federal, state, or local government, including certain multijurisdictional agencies and departments that carry out the business of government
- **explanatoryNote**: Identifying government bodies is a pre-requisite for identifying government officials. This information is needed to help ensure compliance with applicable laws relating to bribery or corruption, including the U.S. Foreign Corrupt Practices Act (FCPA), the UK Bribery Act 2010 (UKBA), the U.S. Bank Bribery Act (Bribery Act), and other anti-bribery and corruption laws in the jurisdictions where financial institutions conduct business.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
