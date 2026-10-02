---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: board of directors
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: group of people comprising the governing body of an organization that has the authority to set organizational strategy
      and policies as well as to select and, to some degree manage, leadership
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For a public, for profit organization, its members (directors) are elected normally by the subscribers (stockholders)
      of the firm (generally at an annual general meeting) to govern the firm and look after the subscribers' interests. In
      the case of a not-for-profit organization, the board ensures the organization is acting in line with its mission. The
      board has the ultimate decision-making authority and, in general, is empowered to (1) set the company's policy, objectives,
      and overall direction, (2) adopt bylaws, (3) name members of the advisory, executive, finance, and other committees,
      (4) hire, monitor, evaluate, and fire the managing director and senior executives, (5) determine and pay the dividend,
      and (6) issue additional shares. Though all its members might not be engaged in the company's day-to-day operations,
      the entire board is held liable (under the doctrine of collective responsibility) for the consequences of the firm's
      policies, actions, and failures to act. Members of the board usually include senior-most executives (called inside directors
      or executive directors) as well as experts or respected persons chosen from the wider community (called outside directors
      or non-executive directors).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CorporateOfficer
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/nominates
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Ncc7ab3117bd843d39858879f585332bd
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nf50e6e0eb98d41da84aa7ba264e32f18
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/EntityControllingParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardOfDirectors
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: board of directors
type: Ontology Class
---

# board of directors

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardOfDirectors>

## Definition

group of people comprising the governing body of an organization that has the authority to set organizational strategy and policies as well as to select and, to some degree manage, leadership

## Relationships

- **Subclass of**: [EntityControllingParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md)

## Constraints

- **[nominates](/concepts/fibo/BE/OwnershipAndControl/Executives/nominates.md)**: some values from of type [CorporateOfficer](/concepts/fibo/BE/OwnershipAndControl/Executives/CorporateOfficer.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Ncc7ab3117bd843d39858879f585332bd`
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nf50e6e0eb98d41da84aa7ba264e32f18`

## Annotations

- **label**: board of directors
- **definition**: group of people comprising the governing body of an organization that has the authority to set organizational strategy and policies as well as to select and, to some degree manage, leadership
- **explanatoryNote**: For a public, for profit organization, its members (directors) are elected normally by the subscribers (stockholders) of the firm (generally at an annual general meeting) to govern the firm and look after the subscribers' interests. In the case of a not-for-profit organization, the board ensures the organization is acting in line with its mission. The board has the ultimate decision-making authority and, in general, is empowered to (1) set the company's policy, objectives, and overall direction, (2) adopt bylaws, (3) name members of the advisory, executive, finance, and other committees, (4) hire, monitor, evaluate, and fire the managing director and senior executives, (5) determine and pay the dividend, and (6) issue additional shares. Though all its members might not be engaged in the company's day-to-day operations, the entire board is held liable (under the doctrine of collective responsibility) for the consequences of the firm's policies, actions, and failures to act. Members of the board usually include senior-most executives (called inside directors or executive directors) as well as experts or respected persons chosen from the wider community (called outside directors or non-executive directors).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
