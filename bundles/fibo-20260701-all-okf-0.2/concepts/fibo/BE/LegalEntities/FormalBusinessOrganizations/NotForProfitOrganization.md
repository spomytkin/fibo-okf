---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: not for profit organization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: organization that uses its surplus revenues to further achieve its purpose rather than distributing its surplus
      income to the organization's owners (directors, investors, and equivalents) as profit / dividends
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the US, a nonprofit organization is an association that explicitly is not required to pay taxes on its income.
      Such organizations are qualified for this exemption due to their socially desirable objective (e.g. hospitals, charitable
      organizations, etc., or because they meet some set of requirements as determined by the US Internal Revenue Service.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The nonprofit landscape is highly varied, although many people have come to associate NPOs with charitable organizations.
      Although charities do comprise an often high profile or visible aspect of the sector, there are many other types of
      nonprofits. Overall, they tend to be either member-serving or community-serving. Member-serving organizations include
      mutual societies, cooperatives, trade unions, credit unions, industry associations, sports clubs, retired serviceman''s
      clubs and other organizations that benefit a particular group of people - the members of the organization. Typically,
      community-serving organizations are focused on providing services to the community in general, either globally or locally:
      organizations delivering human services programs or projects, aid and development programs, medical research, education
      and health services, and so on.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: non-profit organization
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/NotForProfitObjective
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/hasObjective
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/FormalOrganization
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization
sources:
- id: fibo-source-9758af6c79
  resource: references/fibo/BE/LegalEntities/FormalBusinessOrganizations.rdf
  sha256: 9758af6c796f157eedb21d72cde0822cb7a2ecbd6b5a70ef23be48121c598ede
  title: FIBO source BE/LegalEntities/FormalBusinessOrganizations.rdf
title: not for profit organization
type: Ontology Class
---

# not for profit organization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization>

## Definition

organization that uses its surplus revenues to further achieve its purpose rather than distributing its surplus income to the organization's owners (directors, investors, and equivalents) as profit / dividends

## Relationships

- **Subclass of**: [FormalOrganization](<https://www.omg.org/spec/Commons/Organizations/FormalOrganization>)

## Constraints

- **[hasObjective](/concepts/fibo/FND/GoalsAndObjectives/Objectives/hasObjective.md)**: min qualified cardinality 0 of type [NotForProfitObjective](/concepts/fibo/BE/LegalEntities/LegalPersons/NotForProfitObjective.md)

## Annotations

- **label**: not for profit organization
- **definition**: organization that uses its surplus revenues to further achieve its purpose rather than distributing its surplus income to the organization's owners (directors, investors, and equivalents) as profit / dividends
- **explanatoryNote**: In the US, a nonprofit organization is an association that explicitly is not required to pay taxes on its income. Such organizations are qualified for this exemption due to their socially desirable objective (e.g. hospitals, charitable organizations, etc., or because they meet some set of requirements as determined by the US Internal Revenue Service.
- **explanatoryNote**: The nonprofit landscape is highly varied, although many people have come to associate NPOs with charitable organizations. Although charities do comprise an often high profile or visible aspect of the sector, there are many other types of nonprofits. Overall, they tend to be either member-serving or community-serving. Member-serving organizations include mutual societies, cooperatives, trade unions, credit unions, industry associations, sports clubs, retired serviceman's clubs and other organizations that benefit a particular group of people - the members of the organization. Typically, community-serving organizations are focused on providing services to the community in general, either globally or locally: organizations delivering human services programs or projects, aid and development programs, medical research, education and health services, and so on.
- **synonym**: non-profit organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
